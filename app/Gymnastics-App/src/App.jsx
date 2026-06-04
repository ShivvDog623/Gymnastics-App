import { BrowserRouter } from 'react-router-dom';
import SideBar from "./sidebar/SideBar";

function App() {
  return (
    <BrowserRouter>
      <SideBar />
    </BrowserRouter>
  );
}

export default App;