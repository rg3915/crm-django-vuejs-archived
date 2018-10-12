<template>
  <div>
    Index

    Contador: {{ counter }}

    <b-button variant="primary" @click="incrementStore"><i class="fa fa-plus"></i></b-button>
  </div>
</template>

<script>
  export default {
    methods: {
      incrementStore() {
        this.$store.dispatch('increment')
      }
    },
    computed: {
      counter() {
        return this.$store.state.counter
      }
    }
  }

</script>