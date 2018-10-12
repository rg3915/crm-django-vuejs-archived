<template>
  <div>
    Employees
    
    <b-table striped hover :items="items"></b-table>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      items: []
    }
  },
  created(){
    axios.get('http://localhost:8000/api/crm/employee/')
    .then(items => {
      this.items = items.data
    })
  }
}
</script>