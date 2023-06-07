import "./App.css";
import logoImg from "./genemo_logo.png";
import { React, useState, useEffect } from "react";

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

function Main({ firstTtl, secondTtl }) {
  return (
    <main>
      <BigTitle ttl={firstTtl} />
      <SmallTitle ttl={secondTtl} />
    </main>
  );
}

function BigTitle({ ttl }) {
  return <h2>{ttl}</h2>;
}

function SmallTitle({ ttl }) {
  return <h4>{ttl}</h4>;
}

function FormWizard() {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState("");

  const handleChange = (e) => {
    setFormData(e.target.value);
  };

  /*
  useEffect(()=> {
    console.log({formData})
  }, [formData])
  */

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform form submission logic here
    console.log(formData);
  };

  const nextStep = () => {
    setStep(step + 1);
  };

  const skipStep = () => {
    setStep(step + 3);
  };

  const prevStep = () => {
    setStep(step - 1);
  };

  return (
    <main>
      {step === 1 && (
        <div>
          <BigTitle ttl="Concept Writing" />
          <SmallTitle ttl="여러분이 만들고자 하는 이모티콘의 핵심 컨셉을 만들어 주세요" />
          <SmallTitle ttl="tip) 캐릭터의 행동 묘사가 가장 적합합니다." />
          <form onSubmit={nextStep} className="concept-form">
            <label className="concept-label">concept</label>
            <input
              type="text"
              name="concept"
              value={formData}
              onChange={handleChange}
              placeholder="ex)가방을 멘 도라에몽"
              required
              className="description"
            />
            <div className="btnArea">
              <button type="submit" className="bigBtn">
                다음으로
              </button>
            </div>
          </form>
        </div>
      )}

      {step === 2 && (
        <div>
          <a className="previous" onClick={prevStep}>&lt; 이전으로</a>
          <BigTitle ttl="추가 개인화 여부" />
          <SmallTitle ttl="더 개인화된 이모티콘을 생성하기 위해, 이모티콘 별 행동을 묘사 할 수 있습니다." />
          <SmallTitle ttl="생성하기를 누르시면, 설정된 기본 묘사로 이모티콘이 생성됩니다." />
          <div className="btnArea">
            <button type="submit" className="bigBtn" onClick={nextStep}>
              다음으로
            </button>
          </div>
          <div className="btnArea">
            <button type="submit" className="bigBtn" onClick={skipStep}>
              생성하기
            </button>
          </div>
        </div>
      )}

      {step === 3 && (
        <div>
          <BigTitle ttl="감정 설정 하기" />
          <SmallTitle ttl="설정할 감정과 감정표현의 개수를 설정해주세요." />
          <div className="foremotions">
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
            <div className="emotion">
              <div className="emotion-label">기쁨</div>
              <input className= "jang" type="number" />
            </div>
          </div>
        </div>
      )}
    </main>
  );
}

export { Header, Main, FormWizard, BigTitle, SmallTitle };
