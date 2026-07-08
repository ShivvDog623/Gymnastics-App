import { useState } from "react";
import {
    DndContext,
    useDraggable,
    useDroppable,
    useSensor,
    useSensors,
    PointerSensor,
    TouchSensor,
    KeyboardSensor,
    pointerWithin,
} from "@dnd-kit/core";

const EVENTS = ["Vault", "Bars", "Beam", "Floor"];
const EVENT_MAX = 4;
const REFEREE_MAX = 1;
const POOL_ID = "pool";
const REFEREE_ID = "referee";

const ACCENT_CLASSES = {
    indigo: "border-indigo-500 bg-indigo-50",
    amber: "border-amber-500 bg-amber-50",
};

const sampleJudges = [
    { id: "judge-1", name: "Judge 1" },
    { id: "judge-2", name: "Judge 2" },
    { id: "judge-3", name: "Judge 3" },
    { id: "judge-4", name: "Judge 4" },
    { id: "judge-5", name: "Judge 5" },
    { id: "judge-6", name: "Judge 6" },
    { id: "judge-7", name: "Judge 7" },
    { id: "judge-8", name: "Judge 8" },
];

function JudgeChip({ judge }) {
    const { attributes, listeners, setNodeRef, transform, isDragging } = useDraggable({
        id: judge.id,
    });

    return (
        <div
            ref={setNodeRef}
            style={transform ? { transform: `translate3d(${transform.x}px, ${transform.y}px, 0)` } : undefined}
            {...listeners}
            {...attributes}
            className={`badge badge-lg px-4 py-3 cursor-grab active:cursor-grabbing select-none touch-none ${
                isDragging ? "opacity-40 relative z-50" : "bg-indigo-500 text-white border-none"
            }`}
        >
            {judge.name}
        </div>
    );
}

function DropSlot({ id, label, judges, max, accent = "indigo" }) {
    const { setNodeRef, isOver } = useDroppable({ id });
    const isFull = max !== Infinity && judges.length >= max;

    return (
        <div
            ref={setNodeRef}
            className={`rounded-xl border-2 p-3 min-h-[92px] transition-colors ${
                isOver && !isFull ? ACCENT_CLASSES[accent] : "border-gray-300 bg-gray-50"
            }`}
        >
            <div className="flex items-center justify-between mb-2">
                <span className="font-bold text-black">{label}</span>
                <span className={`text-xs font-semibold ${isFull ? "text-error" : "text-gray-500"}`}>
                    {max === Infinity ? judges.length : `${judges.length}/${max}`}
                </span>
            </div>
            <div className="flex flex-wrap gap-2 justify-center">
                {judges.length === 0 && <span className="text-xs text-gray-400">Drop judge here</span>}
                {judges.map((judge) => (
                    <JudgeChip key={judge.id} judge={judge} />
                ))}
            </div>
        </div>
    );
}

function JudgeDragDrop({ judges = sampleJudges }) {
    const [assignments, setAssignments] = useState({
        [REFEREE_ID]: [],
        Vault: [],
        Bars: [],
        Beam: [],
        Floor: [],
    });

    const sensors = useSensors(
        useSensor(PointerSensor, { activationConstraint: { distance: 5 } }),
        useSensor(TouchSensor, { activationConstraint: { delay: 150, tolerance: 5 } }),
        useSensor(KeyboardSensor)
    );

    const assignedIds = new Set(Object.values(assignments).flatMap((slot) => slot.map((j) => j.id)));
    const pool = judges.filter((judge) => !assignedIds.has(judge.id));

    const capacityFor = (slotId) => (slotId === REFEREE_ID ? REFEREE_MAX : EVENT_MAX);

    const handleDragEnd = ({ active, over }) => {
        if (!over) return;

        const judge = judges.find((j) => j.id === active.id);
        if (!judge) return;

        setAssignments((prev) => {
            const next = {};
            for (const slotId of Object.keys(prev)) {
                next[slotId] = prev[slotId].filter((j) => j.id !== judge.id);
            }

            if (over.id === POOL_ID) return next;

            const current = next[over.id] ?? [];
            if (current.length >= capacityFor(over.id)) return prev;

            next[over.id] = [...current, judge];
            return next;
        });
    };

    return (
        <DndContext sensors={sensors} collisionDetection={pointerWithin} onDragEnd={handleDragEnd}>
            <div className="w-full space-y-4 text-left">
                <DropSlot id={REFEREE_ID} label="Referee" judges={assignments[REFEREE_ID]} max={REFEREE_MAX} accent="amber" />

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    {EVENTS.map((event) => (
                        <DropSlot key={event} id={event} label={event} judges={assignments[event]} max={EVENT_MAX} />
                    ))}
                </div>

                <DropSlot id={POOL_ID} label="Unassigned Judges" judges={pool} max={Infinity} />
            </div>
        </DndContext>
    );
}

export default JudgeDragDrop;
