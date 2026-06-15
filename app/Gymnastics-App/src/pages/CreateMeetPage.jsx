function CreateMeetPage() {
    const meets = ["Meet 1", "Meet 2", "Meet 3", "Meet 4", "Meet 5"];

    return (
        <div className="flex flex-col lg:flex-row min-h-screen p-4 md:p-8 gap-6 md:gap-8">
            {/* Left: Select or create a meet */}
            <div className="card w-full lg:w-64 bg-indigo-500 shadow-sm h-fit">
                <div className="card-body items-center text-center gap-4">
                    <h2 className="card-title text-white">Select or create a meet</h2>
                    <div className="card w-full bg-white shadow-sm">
                        <div className="card-body p-2 gap-1">
                            {meets.map((meet, i) => (
                                <button
                                    key={i}
                                    className="btn btn-ghost bg-white justify-start text-left font-bold text-black"
                                >
                                    {meet}
                                </button>
                            ))}
                        </div>
                    </div>
                </div>
            </div>

            {/* Right: Form + buttons */}
            <div className="flex flex-col flex-1 gap-6 md:gap-8">
                {/* Form: 1 column on mobile, 2 columns on md+ */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6">
                    <div className="form-control">
                        <label className="label font-bold">Meet Name</label>
                        <input
                            id="meet-name"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>
                    <div className="form-control">
                        <label className="label font-bold">Meet Director</label>
                        <input
                            id="meet-director"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>

                    <div className="form-control">
                        <label className="label font-bold">Director Email</label>
                        <input
                            id="director-email"
                            type="email"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>
                    <div className="form-control">
                        <label className="label font-bold">Meet Facility Name</label>
                        <input
                            id="meet-facility-name"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>

                    <div className="form-control">
                        <label className="label font-bold">Pro Number</label>
                        <input
                            id="pro-number"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>
                    <div className="form-control">
                        <label className="label font-bold">Host Gym</label>
                        <input
                            id="host-gym"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>

                    <div className="form-control">
                        <label className="label font-bold">Start Date</label>
                        <input
                            id="start-date"
                            type="date"
                            className="input input-bordered w-full"
                        />
                    </div>
                    <div className="form-control">
                        <label className="label font-bold">End Date</label>
                        <input
                            id="end-date"
                            type="date"
                            className="input input-bordered w-full"
                        />
                    </div>

                    <div className="form-control">
                        <label className="label font-bold">Facility Address</label>
                        <input
                            id="facility-address"
                            type="text"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>
                    <div className="form-control">
                        <label className="label font-bold">Judges Per Event</label>
                        <input
                            id="judges-per-event"
                            type="number"
                            placeholder="Placeholder"
                            className="input input-bordered w-full"
                        />
                    </div>
                </div>

                {/* Action buttons */}
                <div className="flex flex-col sm:flex-row justify-center gap-4 md:gap-8 mt-12">
                    <button className="btn btn-lg rounded-full btn-warning text-white border-none px-12 w-full sm:w-auto">
                        Update
                    </button>
                    <button className="btn btn-lg rounded-full btn-success text-white border-none px-12 w-full sm:w-auto">
                        Create
                    </button>
                    <button className="btn btn-lg rounded-full btn-error text-white border-none px-12 w-full sm:w-auto">
                        Delete
                    </button>
                </div>
            </div>
        </div>
    );
}

export default CreateMeetPage;