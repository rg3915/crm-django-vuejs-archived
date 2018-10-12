<template>
  <div>
    Employees
    
    {{ pk }}
    {{ slug }}

  </div>
</template>

<script>

export default {
  data () {
    return {
      items: [],
      deletingItem: {}
    }
  },
}
</script>