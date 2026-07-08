function CoachesCard({ gymName }) {
    return (
        <div className="card bg-indigo-500 shadow-sm">
            <div className="card-body gap-3">
                <h2 className="card-title text-white font-bold">Coaches</h2>
                <div className="card bg-white shadow-sm">
                    <div className="card-body items-center text-center min-h-32">
                        <p className="font-bold text-black">
                            {gymName ? `Coaches for ${gymName}` : "Shows Coaches in Gym"}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CoachesCard;