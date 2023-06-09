import "./App.css";
import logoImg from "./genemo_logo.png";
import { React, useState, useEffect } from "react";

import "react-step-progress-bar/styles.css";
import { ProgressBar, Step } from "react-step-progress-bar";

import axios from "axios";

const MyProgressBar = ({ currentStep }) => {
  return (
    <div
      style={{
        position: "fixed",
        top: 70,
        left: 0,
        width: "100%",
        padding: "0px",
      }}
      className="progressbar-area"
    >
      <ProgressBar
        percent={(currentStep - 1) * 25}
        filledBackground="linear-gradient(to right, #FFC694, #F5600C"
        width="100%;"
      ></ProgressBar>
    </div>
  );
};

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

function BigTitle({ ttl }) {
  return <h2>{ttl}</h2>;
}

function SmallTitle({ ttl }) {
  return <h4>{ttl}</h4>;
}

function MiddleTitle({ ttl }) {
  return (
    <div className="result-title">
      <h4>{ttl}</h4>
    </div>
  );
}

const ImageViewer = ({ imagePaths }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const goToNextImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex + 1) % imagePaths.length);
  };
  const goToPrevImage = () => {
    setCurrentImageIndex(
      (prevIndex) => (prevIndex - 1 + imagePaths.length) % imagePaths.length
    );
  };

  return (
    <div className="img-area">
      <div className="triangle-left" onClick={goToPrevImage}></div>
      <div className="img-box">
        <img
          src={imagePaths[currentImageIndex]}
          alt={`Image ${currentImageIndex}`}
        />
      </div>
      <div className="triangle-right" onClick={goToNextImage}></div>
    </div>
  );
};

function FormWizard() {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState("");
  const [numbers, setNumbers] = useState([0, 0, 0, 0, 0, 0, 0]);
  const [remaining, setRemaining] = useState(32);
  const [mode, setmode] = useState(-1);
  const [descs, setDescs] = useState(Array(7).fill([]));
  const imagePaths = [
    "image0",
    "image1",
    "image2",
    "image3",
    "image4",
    "image5",
    "image6",
  ];

  useEffect(() => {
    setRemaining(
      32 -
        (numbers[0] +
          numbers[1] +
          numbers[2] +
          numbers[3] +
          numbers[4] +
          numbers[5] +
          numbers[6])
    );
  }, [numbers]);

  function Emotion({ type, index }) {
    return (
      <div className="emotion">
        <p className="emotion-label">{type}</p>
        <button onClick={() => handleMinus(index)}>-</button>
        <input
          className="jang"
          type="number"
          value={numbers[index]}
          min="0"
          max="32"
          onChange={(event) => handleNumberChange(event, index)}
        />
        <button onClick={() => handlePlus(index)}>+</button>
      </div>
    );
  }
  const handleMinus = (index) => {
    const updatedNumbers = [...numbers];
    if (updatedNumbers[index] > 0) {
      updatedNumbers[index] -= 1;
      setNumbers(updatedNumbers);
    }
  };

  const handlePlus = (index) => {
    const updatedNumbers = [...numbers];
    updatedNumbers[index] += 1;
    setNumbers(updatedNumbers);
  };

  const handleNumberChange = (event, index) => {
    const updatedNumbers = [...numbers];
    updatedNumbers[index] = parseInt(event.target.value);
    setNumbers(updatedNumbers);
  };

  const handleInputChange = (sectionIndex, inputIndex, event) => {
    const newInputs = [...descs];
    const sectionInputs = [...newInputs[sectionIndex]];
    sectionInputs[inputIndex] = event.target.value;
    newInputs[sectionIndex] = sectionInputs;
    setDescs(newInputs);
  };

  const handleChange = (e) => {
    setFormData(e.target.value);
  };

  useEffect(() => {
    console.log(formData);
  }, [formData]);

  useEffect(() => {
    console.log({ step });
  }, [step]);

  useEffect(() => {
    console.log(descs);
  }, [descs]);

  useEffect(() => {
    console.log(`mode${mode}`);
  }, [mode]);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform form submission logic here
    console.log(formData);
  };

  const nextStep = () => {
    if (step === 2) {
      custommode();
      sendModeToServer();
    }
    if (step === 3) {
      if (remaining < 0) {
        alert("32개 이하만 입력할 수 있습니다.");
        return;
      }
    }
    if (step === 4) {
      sendDataToServer1();
    }
    setStep(step + 1);
  };

  const skipStep = () => {
    if (step === 2) {
      defaultmode();
      setStep(step + 3);
      sendModeToServer();
      sendDataToServer0();
    }
  };

  const prevStep = () => {
    setStep(step - 1);
  };

  const restart = () => {
    setStep(1);
  };

  const custommode = () => {
    setmode("1");
  };

  const defaultmode = () => {
    setmode("0");
  };

  //간편모드랑 커스텀 모드 중 어떤 건지 전송, (2단계에서 어떤 버튼을 누르느냐에 따라.)
  const sendModeToServer = () => {
    axios
      .post("/api/data", { mode })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  //간편 모드(2단계에서 데이터 전송)
  const sendDataToServer0 = () => {
    axios
      .post("/api/data", { formData })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  //커스텀 모드(4단계에서 데이터 전송)
  const sendDataToServer1 = () => {
    axios
      .post("/api/data", { formData, numbers, descs })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <main>
        {step === 1 && (
          <div>
            <MyProgressBar currentStep={step} />
            <BigTitle ttl="Concept Writing" />
            <SmallTitle ttl="여러분이 만들고자 하는 이모티콘의 핵심 컨셉을 만들어 주세요" />
            <SmallTitle ttl="tip) 캐릭터의 행동 묘사가 가장 적합합니다." />
            <form onSubmit={nextStep} className="concept-form">
              <div className="concept-input">
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
              </div>
              <div className="btnArea">
                <button type="submit" className="middleBtn">
                  다음으로
                </button>
              </div>
            </form>
          </div>
        )}

        {step === 2 && (
          <div>
            <a className="previous" onClick={prevStep}>
              &lt; 이전으로
            </a>
            <MyProgressBar currentStep={step} />
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
            <MyProgressBar currentStep={step} />
            <BigTitle ttl="감정 설정 하기" />
            <SmallTitle
              ttl={`설정할 감정과 감정표현의 개수를 설정해주세요. (남은 개수: ${remaining}개)`}
            />
            <div className="foremotions">
              <Emotion type="기쁨" index="0" />
              <Emotion type="슬픔" index="1" />
              <Emotion type="분노" index="2" />
              <Emotion type="공포" index="3" />
              <Emotion type="놀람" index="4" />
              <Emotion type="혐오" index="5" />
              <Emotion type="중립" index="6" />
            </div>
            <div className="btnArea3">
              <button className="smallBtn" onClick={prevStep}>
                이전으로
              </button>
              <button className="smallBtn" onClick={nextStep}>
                다음으로
              </button>
            </div>
          </div>
        )}

        {step === 4 && (
          <div>
            <MyProgressBar currentStep={step} />
            {numbers[0] !== 0 && (
              <div>
                <BigTitle ttl="기쁨" />
                <SmallTitle ttl="'기쁨'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[0] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[0][index] || ""}
                      onChange={(event) => handleInputChange(0, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[1] !== 0 && (
              <div>
                <BigTitle ttl="슬픔" />
                <SmallTitle ttl="'슬픔'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[1] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[1][index] || ""}
                      onChange={(event) => handleInputChange(1, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[2] !== 0 && (
              <div>
                <BigTitle ttl="분노" />
                <SmallTitle ttl="'분노'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[2] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[2][index] || ""}
                      onChange={(event) => handleInputChange(2, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[3] !== 0 && (
              <div>
                <BigTitle ttl="공포" />
                <SmallTitle ttl="'공포'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[3] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[3][index] || ""}
                      onChange={(event) => handleInputChange(3, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[4] !== 0 && (
              <div>
                <BigTitle ttl="놀람" />
                <SmallTitle ttl="'놀람'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[4] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[4][index] || ""}
                      onChange={(event) => handleInputChange(4, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[5] !== 0 && (
              <div>
                <BigTitle ttl="혐오" />
                <SmallTitle ttl="'혐오'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[5] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[5][index] || ""}
                      onChange={(event) => handleInputChange(5, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            {numbers[6] !== 0 && (
              <div>
                <BigTitle ttl="중립" />
                <SmallTitle ttl="'중립'을 위한 이모티콘을 구체적으로 묘사해 주세요" />
                {Array.from({ length: numbers[6] }, (_, index) => (
                  <div className="desc-area" key={index}>
                    <label className="concept-label2">{index + 1}</label>
                    <input
                      type="text"
                      className="description2"
                      value={descs[6][index] || ""}
                      onChange={(event) => handleInputChange(6, index, event)}
                    ></input>
                  </div>
                ))}
              </div>
            )}
            <div className="btnArea2">
              <button className="smallBtn" onClick={prevStep}>
                이전으로
              </button>
              <button className="smallBtn" onClick={nextStep}>
                생성하기
              </button>
            </div>
          </div>
        )}

        {step === 5 && (
          <div className="result-page">
            <MyProgressBar currentStep={step} />
            <MiddleTitle ttl="생성 완료!" />
            <MiddleTitle ttl="고객님만의 이모티콘이 완성되었습니다." />
            <ImageViewer imagePaths={imagePaths} />
            <div className="btnArea2">
              <button className="smallBtn" onClick={restart}>
                다시 생성하기
              </button>
              <button className="smallBtn">이미지 다운 받기</button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export { Header, FormWizard, BigTitle, SmallTitle };
