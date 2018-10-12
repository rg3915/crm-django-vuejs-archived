<template>
  <div>
    Employees
    
    {{ pk }}
    {{ slug }}

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      items: [],
      deletingItem: {}
    }
  },
}
</script>