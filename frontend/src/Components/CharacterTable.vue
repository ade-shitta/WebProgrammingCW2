<template>
  <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Age</th>
          <th>Birth Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="character in characters" :key="character.id">
          <td>{{ character.name }}</td>
          <td>{{ character.description }}</td>
          <td>{{ character.age }}</td>
          <td>{{ character.birth_date || 'Unknown' }}</td>
          <td>
            <button class="btn btn-sm btn-info me-2" @click="$emit('edit', character)">Edit</button>
            <button class="btn btn-sm btn-danger" @click="$emit('delete', character.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    characters: {
      type: Array,
      required: true
    }
  }
}
</script> 