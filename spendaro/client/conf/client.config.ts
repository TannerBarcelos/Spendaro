const APP_PORT = 5173;
const SERVICE_PORT = 8000;

const WITH_SERVICE = true;

const PROXY = {
    service_url: `http://rest-service:${SERVICE_PORT}`,
    local_url: `http://localhost:${SERVICE_PORT}`,
}

const MODE = 'development';

export default {
    APP_PORT,
    SERVICE_PORT,
    WITH_SERVICE,
    PROXY,
    MODE,
}
