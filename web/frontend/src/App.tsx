import { useState } from "react";
import ErrorBoundary from "./components/ErrorBoundary";
import Header from "./components/Header";
import UploadArea from "./components/UploadArea";
import UploadList from "./components/UploadList";

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
      <UploadList />
    </ErrorBoundary>
  );
};

export default App;
