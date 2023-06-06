import "./App.css";
import logoImg from "./genemo_logo.png";

function Header() {
  return (
    <header>
      <div className="logo">
        <img src={logoImg} alt="genego logo" className="logoimg" />
        <a className="logottl" href="index.html">
          Ge-Nemo
        </a>
      </div>
      <ul className="nav-bar">
        <li>
          <a href="concept.html">execute</a>
        </li>
        <li>
          <a href="contribution.html">contribution</a>
        </li>
        <li>
          <a href="about.html">about</a>
        </li>
      </ul>
    </header>
  );
}

function Main() {
  return <main></main>;
}

export { Header, Main };
