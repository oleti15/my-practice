import logo from './logo.svg';
import './App.css';
import CricketScore from './components/CricketScore';
// import AppHeader from './AppHeader';
// import MovieSearch from './MovieSearch';

function App() {
  return (
    <div>
      {<CricketScore target={200} totalOvers={10}  /> } 
      {/* <AppHeader/> */}
      {/* {<MovieSearch/>} */}
      <br></br>
    </div>
  );
}
export default App;
