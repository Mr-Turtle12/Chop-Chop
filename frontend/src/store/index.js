// store/index.js

import { createStore } from 'vuex';


const store = createStore({
  state: {
    websocketUrl: 'ws://localhost:8765', // Start with an empty string or a default value
    HTTPUrl: 'http://localhost:8000/photos/',
  },
  mutations: {
    setWebsocketUrl(state, url) {
      state.websocketUrl = url;
      console.log(state.websocketUrl);
    },
    setHTTPUrl(state, url) {
      state.HTTPUrl = url;
      console.log(state.HTTPUrl);
    },
  },
  actions: {
    setWebsocketUrl({ commit }, url) {
      console.log(url);
      commit('setWebsocketUrl', url);
    },
    setHTTPUrl({ commit }, url) {
      console.log(url);
      commit('setHTTPUrl', url);
    },
  },
  getters: {
    getWebsocketUrl: state => state.websocketUrl,
    getHTTPUrl: state => state.HTTPUrl
  },
});


export default store;
