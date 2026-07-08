import { useState } from "react";

function AgeRangeModal({ isOpen, onClose, ageGroups, onSave }) {
    const [groups, setGroups] = useState(ageGroups);
    const [form, setForm] = useState({ name: "", minAge: "", maxAge: "" });
    const [error, setError] = useState("");

    const addGroup = () => {
        if (!form.name || !form.minAge || !form.maxAge) {
            setError("All fields are required.");
            return;
        }
        if (Number(form.minAge) >= Number(form.maxAge)) {
            setError("Min age must be less than max age.");
            return;
        }
        setError("");
        setGroups([...groups, { ...form, id: Date.now() }]);
        setForm({ name: "", minAge: "", maxAge: "" });
    };

    const removeGroup = (id) => setGroups(groups.filter((g) => g.id !== id));

    const handleSave = () => {
        onSave(groups);
        onClose();
    };

    const handleClose = () => {
        setGroups(ageGroups);
        setForm({ name: "", minAge: "", maxAge: "" });
        setError("");
        onClose();
    };

    return (
        <dialog className={`modal ${isOpen ? "modal-open" : ""}`}>
            <div className="modal-box w-11/12 max-w-2xl">
                <h3 className="font-bold text-xl mb-4">Age Range Groups</h3>

                <div className="space-y-2 mb-4 max-h-48 overflow-y-auto">
                    {groups.length === 0 && (
                        <p className="text-gray-400 text-sm text-center py-4">No age groups added yet.</p>
                    )}
                    {groups.map((g) => (
                        <div key={g.id} className="flex items-center justify-between bg-base-200 rounded px-3 py-2">
                            <span className="font-semibold">{g.name}</span>
                            <span className="text-sm text-gray-500">Ages {g.minAge}–{g.maxAge}</span>
                            <button className="btn btn-xs btn-error" onClick={() => removeGroup(g.id)}>Remove</button>
                        </div>
                    ))}
                </div>

                <div className="grid grid-cols-3 gap-3">
                    <div className="form-control">
                        <label className="label text-sm font-semibold">Group Name</label>
                        <input
                            type="text"
                            placeholder="e.g. Junior"
                            className="input input-bordered"
                            value={form.name}
                            onChange={(e) => setForm({ ...form, name: e.target.value })}
                        />
                    </div>
                    <div className="form-control">
                        <label className="label text-sm font-semibold">Min Age</label>
                        <input
                            type="number"
                            placeholder="e.g. 7"
                            className="input input-bordered"
                            value={form.minAge}
                            onChange={(e) => setForm({ ...form, minAge: e.target.value })}
                        />
                    </div>
                    <div className="form-control">
                        <label className="label text-sm font-semibold">Max Age</label>
                        <input
                            type="number"
                            placeholder="e.g. 10"
                            className="input input-bordered"
                            value={form.maxAge}
                            onChange={(e) => setForm({ ...form, maxAge: e.target.value })}
                        />
                    </div>
                </div>

                {error && <p className="text-error text-sm mt-2">{error}</p>}

                <button className="btn btn-outline mt-3 w-full" onClick={addGroup}>+ Add Group</button>

                <div className="modal-action">
                    <button className="btn btn-error" onClick={handleClose}>Cancel</button>
                    <button className="btn btn-primary" onClick={handleSave}>Save</button>
                </div>
            </div>
            <form method="dialog" className="modal-backdrop">
                <button onClick={handleClose}>close</button>
            </form>
        </dialog>
    );
}

export default AgeRangeModal;
