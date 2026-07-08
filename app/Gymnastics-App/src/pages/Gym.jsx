import { useState } from "react";
import GymList from "../components/gymlist/GymList.jsx";
import DisciplinesCard from "../components/disciplinescard/DisciplinesCard";
import CoachesCard from "../components/coachescard/CoachesCard";

function GymPage() {
    const [selectedGym, setSelectedGym] = useState(null);
    const [selectedDisciplines, setSelectedDisciplines] = useState([]);

    const toggleDiscipline = (d) => {
        setSelectedDisciplines((prev) =>
            prev.includes(d) ? prev.filter((x) => x !== d) : [...prev, d]
        );
    };

    return (
        <div className="min-h-screen p-4 md:p-8 flex flex-col gap-6">
            {/* Main content area */}
            <div className="flex flex-col lg:flex-row gap-6 flex-1">

                {/* Left column: Gym list + Disciplines */}
                <div className="flex flex-col gap-6 w-full lg:w-56">
                    <GymList
                        selectedGym={selectedGym}
                        onSelect={setSelectedGym}
                    />
                    <DisciplinesCard
                        selected={selectedDisciplines}
                        onChange={toggleDiscipline}
                    />
                </div>

                {/* Right column: Form + Coaches */}
                <div className="flex flex-col flex-1 gap-6">
                    {/* Form grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6">
                        <div className="form-control md:col-span-1">
                            <label className="label font-bold">Gym Full Name</label>
                            <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>
                        <div className="form-control">
                            <label className="label font-bold">Zone/Section</label>
                            <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>

                        <div className="form-control">
                            <label className="label font-bold">Abbreviated Name</label>
                            <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>
                        <div className="form-control">
                            <label className="label font-bold">Phone Number</label>
                            <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>

                        <div className="form-control md:col-span-2">
                            <label className="label font-bold">Address Of Gym</label>
                            <input type="text" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>

                        <div className="form-control md:col-span-2">
                            <label className="label font-bold">Email Address</label>
                            <input type="email" placeholder="Placeholder" className="input input-bordered w-full" />
                        </div>
                    </div>

                    {/* Coaches card */}
                    <CoachesCard gymName={selectedGym} />
                </div>
            </div>

            {/* Action buttons */}
            <div className="flex flex-col sm:flex-row justify-center gap-4 md:gap-8">
                <button className="btn btn-lg btn-warning rounded-full px-12 w-full sm:w-auto">
                    Update
                </button>
                <button className="btn btn-lg btn-success rounded-full px-12 w-full sm:w-auto">
                    Create
                </button>
                <button className="btn btn-lg btn-error rounded-full px-12 w-full sm:w-auto">
                    Delete
                </button>
            </div>
        </div>
    );
}

export default GymPage;