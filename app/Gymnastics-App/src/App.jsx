import { BrowserRouter } from 'react-router-dom';
import SideBar from "./components/sidebar/SideBar.jsx";

function App() {
  return (
    <BrowserRouter>
      <SideBar />
    </BrowserRouter>
  );
}

export default App;