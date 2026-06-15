
const cards = [
    { label: "Create Meet", id: "create-meet-admin" },
    { label: "Sessions", id: "sessions-admin" },
    { label: "Gyms Attending", id: "gyms-attending-admin" },
    { label: null },
    { label: "Sync Data", id: "sync-data-admin" },
    { label: null },
    { label: "Gymnasts", id: "gymnasts-admin" },
    { label: "Coaches", id: "coaches-admin" },
    { label: "Judges", id: "judges-admin" },
]


function Admin() {
    return (
        //     <div>
        //         <div id="create-meet" className="card w-50 purple card-xs shadow-sm">
        //             <div className="card-body">
        //                 <h1 className="card-title p-10 justify-center">Create Meet</h1>

        //             </div>
        //         </div>
        //         <div id="create-meet" className="card w-50 purple card-xs shadow-sm">
        //             <div className="card-body">
        //                 <h1 className="card-title p-10 justify-center">Create Meet</h1>

        //             </div>
        //         </div>
        //         <div id="" className="card w-50 purple card-xs shadow-sm">
        //             <div className="card-body">
        //                 <h1 className="card-title p-10 justify-center">Create Meet</h1>

        //             </div>
        //         </div>


        //     </div>

        <div className="p-8 flex align-middle justify-center">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {cards.map((card, i) => (
                    card.label
                        ? <div key={card.label} id={card.id} className="card p-7 w-75 h-40 bg-indigo-400 cursor-pointer hover:bg-indigo-500 transition-colors shadow-xl">
                            <div className="card-body items-center justify-center">
                                <h2 className="card-title text-white text-2xl text-center">{card.label}</h2>
                            </div>
                        </div>
                        : <div key={i} />
                ))}
            </div>
        </div>


    )
}

export default Admin;