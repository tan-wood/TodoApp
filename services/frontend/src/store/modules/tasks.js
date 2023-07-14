import axios from "axios";
import taskService from "../services/taskService";

const state = {
  tasks: null,
  task: null,
};

const getters = {
  stateTasks: (state) => state.tasks,
  stateTask: (state) => state.task,
};

// these are matching the backend api routes that we defined with out fastapi!

const actions = {
  async createTask({ dispatch }, task) {
    //TODO build dtos for these so that we can get some type checking in here
    await axios.post("tasks", task);
    await dispatch("getTasks");
  },
  async getTasks({ commit }) {
    let { data } = await axios.get("tasks");
    // so when it gets the tasks, it uses the mutation to set the tasks
    commit("setTasks", data);
  },
  async viewTask({ commit }, id) {
    let { data } = await axios.get(`task/${id}`);
    commit("setTask", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateTask({}, task) {
    await axios.patch(`task/${task.id}`, task.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteTask({}, id) {
    await axios.delete(`task/${id}`);
  },
};

const mutations = {
  setTasks(state, tasks) {
    state.tasks = tasks;
  },
  setTask(state, task) {
    state.task = task;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};

/*
state - both note and notes default to null. They'll be updated to an object and an array of objects, respectively.
getters - retrieves the values of state.note and state.notes.
actions - each of the actions make an HTTP call via Axios and then a few of them perform a side effect -- i.e, call the relevant mutation to update state or a different action.
mutations - both make changes to the state, which update state.note and state.notes.
 */
