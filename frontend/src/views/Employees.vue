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
  async created(){
    const response = await axios.get('http://localhost:8000/api/crm/employee/')
    this.items = response.data
  }
}
</script>