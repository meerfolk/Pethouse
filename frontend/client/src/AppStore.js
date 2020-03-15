import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    config: null,
  },
  mutations: {
    setConfig(state, config) {
      state.config = config;
    },
  },
  actions: {
    getConfig({ commit }) {
      fetch('/api/config')
        .then(response => response.json())
        .then(json => commit('setConfig', json))
    },
  },
});

export default store;