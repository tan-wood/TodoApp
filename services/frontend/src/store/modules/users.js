import axios from "axios";

const state = {
  user: null,
};

const getters = {
  isAuthenticated: (state) => !!state.user,
  stateUser: (state) => state.user,
};

const actions = {
  // from what I can see, dispatch is used to make another call to
  // another action. and then commit, is a call to a mutation.
  // like after you register, it will log you in but after you
  // viewMe, it will set the user
  async register({ dispatch }, form) {
    await axios.post("register", form);
    let UserForm = new FormData();
    UserForm.append("username", form.username);
    UserForm.append("password", form.password);
    await dispatch("login", UserForm);
  },
  async logIn({ dispatch }, user) {
    await axios.post("login", user);
    await dispatch("viewMe");
  },
  async viewMe({ commit }) {
    let { data } = await axios.get("users/whoami");
    await commit("setUser", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
};

const mutations = {
  setUser(state, user) {
    state.user = user;
  },
  logout(state, user) {
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};

/*
isAuthenticated - returns true if state.user is not null and false otherwise.
stateUser - returns the value of state.user.
register - sends a POST request to the /register endpoint we created in the backend, creates a FormData instance, and dispatches it to the logIn action to log the registered user in.
*/
