import { useState } from "react";

const MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
];
const DAYS = Array.from({ length: 31 }, (_, i) => i + 1);
const CURRENT_YEAR = new Date().getFullYear();
const YEARS = Array.from({ length: 100 }, (_, i) => CURRENT_YEAR - i);

const emptyForm = {
    name: "",
    type: "age",
    minAge: "",
    maxAge: "",
    minBirthDate: { day: "", month: "", year: "" },
    maxBirthDate: { day: "", month: "", year: "" },
};

function AgeRangeModal({ isOpen, onClose, ageGroups, onSave }) {
    const [groups, setGroups] = useState(ageGroups);
    const [form, setForm] = useState(emptyForm);
    const [error, setError] = useState("");

    const addGroup = () => {
        if (!form.name) {
            setError("Group name is required.");
            return;
        }

        if (form.type === "age") {
            if (!form.minAge || !form.maxAge) {
                setError("Both min and max age are required.");
                return;
            }
            if (Number(form.minAge) >= Number(form.maxAge)) {
                setError("Min age must be less than max age.");
                return;
            }
        } else {
            const { day: minDay, month: minMonth, year: minYear } = form.minBirthDate;
            const { day: maxDay, month: maxMonth, year: maxYear } = form.maxBirthDate;
            if (!minDay || !minMonth || !minYear || !maxDay || !maxMonth || !maxYear) {
                setError("All birthdate fields are required.");
                return;
            }
            const minDate = new Date(minYear, minMonth - 1, minDay);
            const maxDate = new Date(maxYear, maxMonth - 1, maxDay);
            if (minDate >= maxDate) {
                setError("Min birthdate must be before max birthdate.");
                return;
            }
        }

        setError("");
        setGroups([...groups, { ...form, id: Date.now() }]);
        setForm({ ...emptyForm, type: form.type });
    };

    const removeGroup = (id) => setGroups(groups.filter((g) => g.id !== id));

    const handleSave = () => {
        onSave(groups);
        onClose();
    };

    const handleClose = () => {
        setGroups(ageGroups);
        setForm(emptyForm);
        setError("");
        onClose();
    };

    const formatBirthDate = (bd) => `${bd.month}/${bd.day}/${bd.year}`;

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
                            <span className="text-sm text-gray-500">
                                {g.type === "birthdate"
                                    ? `Born ${formatBirthDate(g.minBirthDate)} – ${formatBirthDate(g.maxBirthDate)}`
                                    : `Ages ${g.minAge}–${g.maxAge}`}
                            </span>
                            <button className="btn btn-xs btn-error" onClick={() => removeGroup(g.id)}>Remove</button>
                        </div>
                    ))}
                </div>

                <div className="form-control mb-3">
                    <label className="label text-sm font-semibold">Group Name</label>
                    <input
                        type="text"
                        placeholder="e.g. Junior"
                        className="input input-bordered"
                        value={form.name}
                        onChange={(e) => setForm({ ...form, name: e.target.value })}
                    />
                </div>

                <div className="tabs tabs-boxed mb-3 w-fit">
                    <a
                        className={`tab ${form.type === "age" ? "tab-active" : ""}`}
                        onClick={() => setForm({ ...form, type: "age" })}
                    >
                        Age Range
                    </a>
                    <a
                        className={`tab ${form.type === "birthdate" ? "tab-active" : ""}`}
                        onClick={() => setForm({ ...form, type: "birthdate" })}
                    >
                        Birth Date
                    </a>
                </div>

                {form.type === "age" ? (
                    <div className="grid grid-cols-2 gap-3">
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
                ) : (
                    <div className="grid grid-cols-2 gap-4">
                        <div className="form-control">
                            <label className="label text-sm font-semibold">Min Birthdate</label>
                            <div className="grid grid-cols-3 gap-2">
                                <select
                                    className="select select-bordered"
                                    value={form.minBirthDate.month}
                                    onChange={(e) => setForm({ ...form, minBirthDate: { ...form.minBirthDate, month: e.target.value } })}
                                >
                                    <option value="" disabled>Month</option>
                                    {MONTHS.map((m, i) => <option key={m} value={i + 1}>{m}</option>)}
                                </select>
                                <select
                                    className="select select-bordered"
                                    value={form.minBirthDate.day}
                                    onChange={(e) => setForm({ ...form, minBirthDate: { ...form.minBirthDate, day: e.target.value } })}
                                >
                                    <option value="" disabled>Day</option>
                                    {DAYS.map((d) => <option key={d} value={d}>{d}</option>)}
                                </select>
                                <select
                                    className="select select-bordered"
                                    value={form.minBirthDate.year}
                                    onChange={(e) => setForm({ ...form, minBirthDate: { ...form.minBirthDate, year: e.target.value } })}
                                >
                                    <option value="" disabled>Year</option>
                                    {YEARS.map((y) => <option key={y} value={y}>{y}</option>)}
                                </select>
                            </div>
                        </div>
                        <div className="form-control">
                            <label className="label text-sm font-semibold">Max Birthdate</label>
                            <div className="grid grid-cols-3 gap-2">
                                <select
                                    className="select select-bordered"
                                    value={form.maxBirthDate.month}
                                    onChange={(e) => setForm({ ...form, maxBirthDate: { ...form.maxBirthDate, month: e.target.value } })}
                                >
                                    <option value="" disabled>Month</option>
                                    {MONTHS.map((m, i) => <option key={m} value={i + 1}>{m}</option>)}
                                </select>
                                <select
                                    className="select select-bordered"
                                    value={form.maxBirthDate.day}
                                    onChange={(e) => setForm({ ...form, maxBirthDate: { ...form.maxBirthDate, day: e.target.value } })}
                                >
                                    <option value="" disabled>Day</option>
                                    {DAYS.map((d) => <option key={d} value={d}>{d}</option>)}
                                </select>
                                <select
                                    className="select select-bordered"
                                    value={form.maxBirthDate.year}
                                    onChange={(e) => setForm({ ...form, maxBirthDate: { ...form.maxBirthDate, year: e.target.value } })}
                                >
                                    <option value="" disabled>Year</option>
                                    {YEARS.map((y) => <option key={y} value={y}>{y}</option>)}
                                </select>
                            </div>
                        </div>
                    </div>
                )}

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
