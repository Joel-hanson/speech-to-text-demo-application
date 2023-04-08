import { useState } from "react";
import ErrorBoundary from "./components/ErrorBoundary";
import Header from "./components/Header";
import UploadArea from "./components/UploadArea";

const App = () => {
  const [uploadedFile, setFile] = useState("");

  const handleFileUpload = (file: string) => {
    setFile(file);
  };

  return (
    <ErrorBoundary>
      <div>
        <Header>
          <UploadArea handleFileUpload={handleFileUpload} uploadedFile={uploadedFile} />
        </Header>
        {/* <Prose /> */}
      </div>
    </ErrorBoundary>
  );
};

export default App;
