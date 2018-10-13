import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

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
    },
    deleteEmployee(state, payload) {
      // axios.delete('http://localhost:8000/api/crm/employee/' + this.deletingItem.pk)
      // .then(response => {
        const idx = state.employees.indexOf(payload)
        state.employees.splice(idx, 1)
      // })
    }
  },
  getters: {
    getEmployeeById (state) {
      return (id) => {
        return state.employees.find(e => {
          return e.pk === id
        })
      }
    }
  },
  actions: {
    increment({ commit }) {
      commit('increment')
    },
    decrement({ commit }) {
      commit('decrement')
    },
    async getEmployees({ commit }) {
      const response = await axios.get('http://localhost:8000/api/crm/employee/')
      const employees = response.data.map(item => {
        return {
          'pk': item.pk,
          'slug': item.slug,
        }
      })
      commit('setEmployees', employees)
    },
    deleteEmployee({ commit }, payload) {
      commit('deleteEmployee', payload)
    }
  }
})