import wretch from "wretch";
import FormDataAddon from "wretch/addons/formData";

export const ORIGIN = document.location.origin;
export const API_URL = ORIGIN + "/api/";
export const WS_URL = ORIGIN.replace(/^http/, "ws") + "/ws/";
export const UPLOAD_API_URL = API_URL + "upload/";

export const getDataFromApi = async (url: string) => {
    const response = await wretch(url).get().json();
    return response;
};

export const getUploadedFiles = async () => {
    const response = await getDataFromApi(API_URL + "files");
    return response;
};

export const uploadFileToApi = async (file: File) => {
    console.log("Uploading file: ", file);
    console.log("URL: ", UPLOAD_API_URL);
    const response = await wretch(UPLOAD_API_URL).addon(FormDataAddon).formData({ file: file }).post().json();
    return response;
};
