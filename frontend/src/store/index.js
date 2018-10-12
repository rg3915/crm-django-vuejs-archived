import Vue from 'vue'
import Vuex from 'vuex'

Vue.use (Vuex)

export default new Vuex.Store ({
  state: {
    counter: 0
  },
  mutations: {
    increment(state){
      state.counter++;
    },
    decrement(state){
      state.counter--;
    }
  },
  actions: {
    increment(obj){
      obj.commit('increment')
    },
    decrement(obj){
      obj.commit('decrement')
    },
  }
})