<template>
  <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Title</th>
          <th>Description</th>
          <th>Episodes</th>
          <th>Status</th>
          <th>Rating</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="anime in animes" :key="anime.id">
          <td>{{ anime.title }}</td>
          <td>{{ anime.description }}</td>
          <td>{{ anime.episodes }}</td>
          <td>{{ anime.is_ongoing ? 'Ongoing' : 'Completed' }}</td>
          <td>{{ anime.rating }}/10</td>
          <td>
            <button class="btn btn-sm btn-info me-2" @click="$emit('edit', anime)">Edit</button>
            <button class="btn btn-sm btn-danger" @click="$emit('delete', anime.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    animes: {
      type: Array,
      required: true
    }
  }
}
</script> 