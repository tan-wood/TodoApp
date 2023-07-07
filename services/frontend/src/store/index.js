import { createStore } from "vuex";

import tasks from "./modules/tasks";
import users from "./modules/users";

export default createStore({
  modules: {
    tasks,
    users,
  },
});

//Here, we created a new Vuex Store with two modules, tasks.js and users.js.
