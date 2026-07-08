import { useState } from "react";
import MeetSessionTree from "../components/meetsessiontree/MeetSessionTree";
import AgeRangeModal from "../components/agerangemodal/AgeRangeModal";
import JudgeDragDrop from "../components/judgedragdrop/JudgeDragDrop";

const sampleTreeData = [
    { type: "file", name: "resume.pdf" },
    {
        type: "folder",
        name: "My Files",
        children: [
            { type: "file", name: "Project-final.psd" },
            { type: "file", name: "Project-final-2.psd" },
            {
                type: "folder",
                name: "Images",
                children: [
                    { type: "image", name: "Screenshot1.png" },
                    { type: "image", name: "Screenshot2.png" },
                ],
            },
        ],
    },
    { type: "file", name: "reports-final-2.pdf" },
];

const initialForm = {
    session_number: "",
    session_description: "",
    session_date: "",
    open_warmup: "",
    timed_warmup: "",
    march_in: "",
    awards: "",
    event_group: "",
    number_of_flights: "",
    rotation_type: "",
};

function Session() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [ageGroups, setAgeGroups] = useState([]);
    const [isAgeModalOpen, setIsAgeModalOpen] = useState(false);
    const [form, setForm] = useState(initialForm);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm((prev) => ({ ...prev, [name]: value }));
    };

    return (
        <div className="p-4 md:p-8 grid grid-cols-1 lg:grid-cols-3 gap-6 md:gap-8">
            {/* Tree for Meet and Session */}
            <div className="card bg-indigo-500 shadow-sm lg:col-span-1">
                <div className="card-body">
                    <MeetSessionTree
                        data={sampleTreeData}
                        onSelect={(node) => setSelectedFile(node)}
                        selectedName={selectedFile?.name}
                    />
                </div>
            </div>

            {/* Form fields */}
            <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6">
                <div className="form-control">
                    <label className="label font-bold">Session Number</label>
                    <input name="session_number" type="number" placeholder="e.g. 1" className="input input-bordered w-full" value={form.session_number} onChange={handleChange} />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Description</label>
                    <input name="session_description" type="text" placeholder="Optional" className="input input-bordered w-full" value={form.session_description} onChange={handleChange} />
                </div>

                <div className="form-control">
                    <label className="label font-bold">Session Date</label>
                    <input name="session_date" type="date" className="input input-bordered w-full" value={form.session_date} onChange={handleChange} />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Event Group</label>
                    <input name="event_group" type="text" placeholder="Optional" className="input input-bordered w-full" value={form.event_group} onChange={handleChange} />
                </div>

                <div className="form-control">
                    <label className="label font-bold">Open Warmup</label>
                    <input name="open_warmup" type="time" className="input input-bordered w-full" value={form.open_warmup} onChange={handleChange} />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Timed Warmup</label>
                    <input name="timed_warmup" type="time" className="input input-bordered w-full" value={form.timed_warmup} onChange={handleChange} />
                </div>

                <div className="form-control">
                    <label className="label font-bold">March In</label>
                    <input name="march_in" type="time" className="input input-bordered w-full" value={form.march_in} onChange={handleChange} />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Awards</label>
                    <input name="awards" type="time" className="input input-bordered w-full" value={form.awards} onChange={handleChange} />
                </div>

                <div className="form-control">
                    <label className="label font-bold">Number of Flights</label>
                    <input name="number_of_flights" type="number" placeholder="Optional" className="input input-bordered w-full" value={form.number_of_flights} onChange={handleChange} />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Rotation Type</label>
                    <input name="rotation_type" type="text" placeholder="Optional" className="input input-bordered w-full" value={form.rotation_type} onChange={handleChange} />
                </div>
            </div>

            {/* Age Range Modal Button */}
            <div className="lg:col-start-2 lg:col-span-2 flex justify-center">
                <button
                    className="btn btn-primary w-full max-w-xs py-6 h-auto text-lg font-bold whitespace-normal ring-offset-2"
                    onClick={() => setIsAgeModalOpen(true)}
                >
                    Age Range Groups {ageGroups.length > 0 && `(${ageGroups.length})`}
                </button>
            </div>

            <AgeRangeModal
                isOpen={isAgeModalOpen}
                onClose={() => setIsAgeModalOpen(false)}
                ageGroups={ageGroups}
                onSave={setAgeGroups}
            />

            {/* Judge Drag and Drop */}
            <div className="card bg-white border-4 border-indigo-500 shadow-sm lg:col-span-3">
                <div className="card-body">
                    <h2 className="text-2xl font-bold text-black mb-4 text-center">
                        Assign Judges
                    </h2>
                    <JudgeDragDrop />
                </div>
            </div>
        </div>
    );
}

export default Session;
