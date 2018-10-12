import Vue from 'vue'
import Vuex from 'vuex'

Vue.use (Vuex)

export default new Vuex.Store ({
  state: {
    counter: 0,
    employees: []
  },
  mutations: {
    increment(state) {
      state.counter++;
    },
    decrement(state) {
      state.counter--;
    },
    setEmployees(state, payload) {
      state.employees = payload
    }
  },
  actions: {
    increment({ commit }) {
      commit('increment')
    },
    decrement({ commit }) {
      commit('decrement')
    },
    getEmployees({ commit }) {
      
    }
  }
})