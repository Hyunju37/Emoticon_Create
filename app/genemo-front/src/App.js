import "./App.css";
import logoImg from "./genemo_logo.png";
import { React, useState, useEffect } from "react";

import "react-step-progress-bar/styles.css";
import { ProgressBar, Step } from "react-step-progress-bar";

import axios from "axios";

import { saveAs } from "file-saver";

const MyProgressBar = ({ currentStep }) => {
  return (
    <div className="bar-area">
      <div
        style={{
          position: "fixed",
          top: 70,
          width: "50%",
        }}
        className="progressbar-area"
      >
        <ProgressBar
          percent={(currentStep - 1) * 20}
          filledBackground="linear-gradient(to right, #FFC694, #F5600C"
          width="100%;"
        >
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Concept
              </div>
            )}
          </Step>
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Select Mode
              </div>
            )}
          </Step>
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Set Emotions
              </div>
            )}
          </Step>
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Describe Emoticon
              </div>
            )}
          </Step>
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Create Emoticon
              </div>
            )}
          </Step>
          <Step transition="scale">
            {({ accomplished, index }) => (
              <div
                className={`indexedStep ${
                  accomplished ? "accomplished" : null
                }`}
              >
                {index + 1}. Get Your Emoticon
              </div>
            )}
          </Step>
        </ProgressBar>
      </div>
    </div>
  );
};

function Header() {
  const [modal, setModal] = useState(false);
  const toggleModal = () => {
    setModal(!modal);
  };

  return (
    <div>
      <header>
        <div className="logo">
          <img src={logoImg} alt="genego logo" className="logoimg" />
          <a className="logottl">Ge-Nemo</a>
        </div>
        <ul className="nav-bar">
          <li>
            <a href="#" onClick={toggleModal}>
              about
            </a>
          </li>
        </ul>
      </header>
      {modal && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={toggleModal}>
              &times;
            </span>
            <h4>Ge-Nemo 가이드</h4>
            <p>Ge-Nemo의 간편 모드는 Plutchik의 '감정 휠'을 기반으로 하며</p>
            <p>개인화 모드는 Paul Ekman의 6가지 기본 감정을 기반으로 합니다.</p>
            <p>기본 감정보다 구체적인 감정이나</p>
            <p>표현하고 싶은 특정 이미지가 있다면</p>
            <p>개인화 모드를 이용하시면 됩니다.</p>
          </div>
        </div>
      )}
    </div>
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

function FormWizard() {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState("");
  const [numbers, setNumbers] = useState([0, 0, 0, 0, 0, 0, 0]);
  const [remaining, setRemaining] = useState(32);
  const [mode, setmode] = useState(-1);
  const [descs, setDescs] = useState(Array(7).fill([]));

  //const [fromflask, setFromFlask] = useState([]);

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
        <button onClick={() => handleMinus(index)} className="num-btn">
          -
        </button>
        <input
          className="jang"
          type="number"
          value={numbers[index]}
          min="0"
          max="32"
          onChange={(event) => handleNumberChange(event, index)}
        />
        <button onClick={() => handlePlus(index)} className="num-btn">
          +
        </button>
      </div>
    );
  }
  const LoadingPage = () => {
    return (
      <div>
        <MiddleTitle ttl="생성중..." />
        <div className="img-area">
          <div class="dots box">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
          </div>
        </div>
      </div>
    );
  };
  const ImageViewer = () => {
    const [currentImageIndex, setCurrentImageIndex] = useState(1);
    const [imageUrl, setImageUrl] = useState("");

    useEffect(() => {
      const getImageUrl = async () => {
        try {
          const response = await axios.get(`/img/${currentImageIndex}`);
          //let blob = new Blob([new ArrayBuffer(response.data)], {type:"image/jpg"});
          //console.log(response.data);
          //setImageUrl(window.URL.createObjectURL(blob));
          setImageUrl(`/img/${currentImageIndex}`);
        } catch (error) {
          console.error(error);
        }
      };
      getImageUrl();
    }, [currentImageIndex]);

    const goToNextImage = () => {
      setCurrentImageIndex((prevIndex) => ((prevIndex % 32) + 1));
    };
    const goToPrevImage = () => {
      setCurrentImageIndex((prevIndex) => (((prevIndex + 30) % 32) + 1));
    };
    return (
      <div>
        <MiddleTitle ttl="생성 완료!" />
        <MiddleTitle ttl="고객님만의 이모티콘이 완성되었습니다." />
        <div className="img-area">
          <div className="triangle-left" onClick={goToPrevImage}></div>
          <div className="img-box">
            <img src={imageUrl} alt={`Image${currentImageIndex}`} />
          </div>
          <div className="triangle-right" onClick={goToNextImage}></div>
        </div>
        <p className="nth-img">{`${currentImageIndex}/32`}</p>
        <div className="btnArea2">
          <button className="smallBtn" onClick={restart}>
            다시 생성하기
          </button>
          <button className="smallBtn" onClick={downloadImages}>
            이미지 다운 받기
          </button>
        </div>
      </div>
    );
  };

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
  const downloadImages = async () => {
    try {
      const response = await axios.get("/img/download", {
        responseType: "blob",
      });
      const url = URL.createObjectURL(response.data);
      const link = document.createElement("a");
      link.href = url;
      link.download = "images.zip";
      link.click();
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    console.log(formData);
  }, [formData]);

  useEffect(() => {
    console.log({ step });
    if (step === 5) {
      getDataFromServer();
    }
  }, [step]);
  /*
  useEffect(() => {
    console.log(descs);
  }, [descs]);
*/
  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform form submission logic here
    console.log(formData);
  };

  const nextStep = () => {
    if (step === 2) {
      setmode(1);
    }
    else if (step === 3) {
      if (remaining !== 0) {
        alert("이미지는 총 32장이어야 합니다.");
        return;
      }
    }
    else if (step === 4) {
      sendDataToServer1();
      //sendDataCustom();
    }
    setStep(step + 1);
  };

  const skipStep = () => {
    if (step === 2) {
      setmode(0);
      //sendModeToServer(0);
      sendDataToServer0();
      //sendDataDefault();
      setStep(step + 3);
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

  //간편 모드(2단계에서 데이터 전송)

  const sendDataToServer0 = () => {
    const info = JSON.stringify({
      mode: 0,
      formData: formData,
    });
    axios
      .post("/", info, { headers: { "Content-Type": "application/json" } })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  //커스텀 모드(4단계에서 데이터 전송)

  const sendDataToServer1 = () => {
    const info = JSON.stringify({
      mode: 1,
      formData: formData,
      numbers: numbers,
      descs: descs,
    });

    axios
      .post("/", info, { headers: { "Content-Type": "application/json" } })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  //이미지가 모두 생성될 때까지 기다림
  const getDataFromServer = async () => {
    var response = setInterval(()=> {
      var w = axios.get('/yet')
      if(w.data === 'done') {
        nextStep();
        clearInterval(response)
      }
    }, 1000);
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
            <form onSubmit={nextStep}>
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
                        required
                      />
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
                        required
                      />
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
                        required
                      />
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
                        required
                      />
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
                        required
                      />
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
                        required
                      />
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
                        required
                      />
                    </div>
                  ))}
                </div>
              )}
              <div className="btnArea2">
                <button className="smallBtn" onClick={prevStep}>
                  이전으로
                </button>
                <button className="smallBtn" type="submit">
                  생성하기
                </button>
              </div>
            </form>
          </div>
        )}

        {step === 5 && (
          <div className="result-page">
            <MyProgressBar currentStep={step} />
            <LoadingPage />
          </div>
        )}

        {step === 6 && (
          <div className="result-page">
            <MyProgressBar currentStep={step} />
            <ImageViewer />
          </div>
        )}
      </main>
    </div>
  );
}

export { Header, FormWizard };
