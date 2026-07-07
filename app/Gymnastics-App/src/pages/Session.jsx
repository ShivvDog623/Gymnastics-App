import { useState } from "react";
import MeetSessionTree from "../meetsessiontree/MeetSessionTree";
import AgeRangeModal from "./AgeRangeModal";
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

function Session() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [ageGroups, setAgeGroups] = useState([]);
    const [isAgeModalOpen, setIsAgeModalOpen] = useState(false);

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
                    <label className="label font-bold">Session</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Description</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>

                <div className="form-control">
                    <label className="label font-bold">Open Warmup</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Timed Warmup</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>

                <div className="form-control">
                    <label className="label font-bold">March In</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Awards</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>

                <div className="form-control">
                    <label className="label font-bold">March In</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>
                <div className="form-control">
                    <label className="label font-bold">Flights</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>

                <div className="form-control">
                    <label className="label font-bold">Rotation Type</label>
                    <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                </div>

                {/* Age Range Modal Button */}
                <button
                    className="btn btn-primary h-auto min-h-20 text-lg font-bold whitespace-normal ring-offset-2"
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
            <div className="card bg-white border-4 border-indigo-500 shadow-sm lg:col-span-2">
                <div className="card-body items-center text-center">
                    <h2 className="text-2xl font-bold text-black">
                        Judge Drag and Drop for events for the sessions after chosen,
                        refer to ProScore for events and set up
                    </h2>
                </div>
            </div>
        </div>
    );
}

export default Session;