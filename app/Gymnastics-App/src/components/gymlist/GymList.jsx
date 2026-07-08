// Hard Coded for now
const gyms = ["Gym 1", "Gym 2", "Gym 3", "Gym 4", "Gym 5"];

function GymList({ selectedGym, onSelect }) {
    return (
        <div className="card bg-indigo-500 shadow-sm">
            <div className="card-body items-center text-center gap-4">
                <h2 className="card-title text-white font-bold">Gym Name Short</h2>
                <div className="card w-full bg-white shadow-sm">
                    <div className="card-body p-2 gap-1">
                        {gyms.map((gym, i) => (
                            <button
                                key={i}
                                onClick={() => onSelect(gym)}
                                className={`btn btn-ghost justify-start text-left font-bold hover:bg-gray-100 ${selectedGym === gym ? "bg-indigo-100 text-indigo-600" : "text-black"
                                    }`}
                            >
                                {gym}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default GymList;