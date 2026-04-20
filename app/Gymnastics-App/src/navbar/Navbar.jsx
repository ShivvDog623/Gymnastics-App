
import { useState } from "react";


function NavBar() {

    return (<div>

        <div id="navbar" className="navbar navy-blue shadow-sm">
            <div className="navbar-start">
                <a className="btn btn-ghost text-xl">StickScore</a>
            </div>
            <div className="navbar-end">
                <button className="btn bg-blue-600">Login</button>
            </div>
        </div>
    </div>);
}


export default NavBar