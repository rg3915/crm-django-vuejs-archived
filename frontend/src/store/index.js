import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import employees from './employees'

// Se fosse index2.js deveria ser 
// import employees from './employees/index2'

Vue.use (Vuex)


export default new Vuex.Store ({
  modules: {
    employees
  },
  state: {
    counter: 0
  },
  mutations: {
    increment(state) {
      state.counter++;
    },
    decrement(state) {
      state.counter--;
    }
  },
  actions: {
    increment({ commit }) {
      commit('increment')
    },
    decrement({ commit }) {
      commit('decrement')
    }
  }
})