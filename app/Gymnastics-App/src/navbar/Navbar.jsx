function NavBar() {
    return (
        <div id="navbar" className="navbar navy-blue shadow-sm">
            <div className="navbar-start">
                <label htmlFor="my-drawer-4" className="btn btn-square btn-ghost">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" strokeLinejoin="round" strokeLinecap="round" strokeWidth="2" fill="none" stroke="currentColor" className="inline-block size-4">
                        <path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"></path>
                        <path d="M9 4v16"></path>
                        <path d="M14 10l2 2l-2 2"></path>
                    </svg>
                </label>
                <a className="btn btn-ghost text-xl">StickScore</a>
            </div>
            <div className="navbar-end">
                <button className="btn bg-blue-500 hover:bg-blue-600">Login</button>
            </div>
        </div>
    )
}

export default NavBar;