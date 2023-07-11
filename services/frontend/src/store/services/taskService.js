import axios from "axios";


export default {
    data() {
        return {};
    },
    async getTask(id) {
        return await axios.get(`task/${id}`);
    }
}