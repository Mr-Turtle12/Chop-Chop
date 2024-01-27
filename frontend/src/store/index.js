// store/index.js

import { createStore } from 'vuex';


const store = createStore({
  state: {
    websocketUrl: 'ws://localhost:8765', // Start with an empty string or a default value
  },
  mutations: {
    setWebsocketUrl(state, url) {
      state.websocketUrl = url;
      console.log(state.websocketUrl);
    },
  },
  actions: {
    setWebsocketUrl({ commit }, url) {
      console.log(url);
      commit('setWebsocketUrl', url);
    },
  },
  getters: {
    getWebsocketUrl: state => state.websocketUrl,
  },
});


export default store;
