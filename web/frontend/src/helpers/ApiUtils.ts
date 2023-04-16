import wretch from "wretch";
import FormDataAddon from "wretch/addons/formData";

export const ORIGIN = document.location.origin;
export const API_URL = ORIGIN + "/api/";
export const WS_URL = ORIGIN.replace(/^http/, "ws") + "/ws/";
export const S2T_WS_URL = WS_URL + "s2t/";
export const UPLOAD_API_URL = API_URL + "upload/";

export const getDataFromApi = async (url: string) => {
    const response = await wretch(url).get().json();
    return response;
};

export const getUploadedFiles = async () => {
    const response = await getDataFromApi(UPLOAD_API_URL);
    return response;
};

export const getDetailedListOfUploads = async () => {
    let api = UPLOAD_API_URL + "task_runs/";
    const response = await getDataFromApi(api);
    return response;
};

export const uploadFileToApi = async (file: File) => {
    const response = await wretch(UPLOAD_API_URL).addon(FormDataAddon).formData({ file: file }).post().json();
    return response;
};
