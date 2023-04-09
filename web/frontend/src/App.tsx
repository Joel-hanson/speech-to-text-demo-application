import { useState } from "react";
import ErrorBoundary from "./components/ErrorBoundary";
import Header from "./components/Header";
import Main from "./components/Main";
import UploadArea from "./components/UploadArea";

const App = () => {
  const [uploadedFile, setFile] = useState<File | undefined>(undefined);

  const handleFileUpload = (file: File | undefined) => {
    setFile(file);
  };

  return (
    <ErrorBoundary>
      <Header>
        <UploadArea handleFileUpload={handleFileUpload} uploadedFile={uploadedFile} />
      </Header>
      <Main />
    </ErrorBoundary>
  );
};

export default App;
