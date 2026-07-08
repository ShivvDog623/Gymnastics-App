import { useState } from "react";

// Hard Coded for now
const disciplines = ["Womens", "Men", "Rhythmic", "Acro"];

function DisciplinesCard({ selected, onChange }) {
    return (
        <div className="card bg-indigo-500 shadow-sm">
            <div className="card-body items-center text-center gap-4">
                <h2 className="card-title text-white font-bold">Disciplines</h2>
                <div className="card w-full bg-white shadow-sm">
                    <div className="card-body p-3 gap-2">
                        {disciplines.map((d, i) => (
                            <label key={i} className="flex items-center gap-3 cursor-pointer">
                                <input
                                    type="checkbox"
                                    className="checkbox checkbox-sm checkbox-neutral"
                                    checked={selected.includes(d)}
                                    onChange={() => onChange(d)}
                                />
                                <span className="font-semibold text-black">{d}</span>
                            </label>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default DisciplinesCard;