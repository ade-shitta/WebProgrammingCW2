<template>
  <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Character</th>
          <th>Anime</th>
          <th>Role</th>
          <th>First Appearance</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="role in roles" :key="role.id">
          <td>{{ role.character.name }}</td>
          <td>{{ role.anime.title }}</td>
          <td>{{ getRoleDisplay(role.role) }}</td>
          <td>Episode {{ role.appearance_episode }}</td>
          <td>
            <button class="btn btn-sm btn-info me-2" @click="$emit('edit', role)">Edit</button>
            <button class="btn btn-sm btn-danger" @click="$emit('delete', role.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    roles: {
      type: Array,
      required: true
    }
  },
  methods: {
    getRoleDisplay(role) {
      const roles = {
        'MC': 'Main Character',
        'SC': 'Supporting Character',
        'ANT': 'Antagonist',
        'GC': 'Guest Character'
      }
      return roles[role]
    }
  }
}
</script> 