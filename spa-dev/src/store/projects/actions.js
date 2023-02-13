import { fetchCheckPoints, fetchProjects } from 'boot/api/project';

export async function getProjects({ commit }) {
  const projects = await fetchProjects();
  commit('setProjects', projects);
}

export async function getCheckPoints({ commit }) {
  const checkPoints = await fetchCheckPoints();
  commit('setCheckPoints', checkPoints);
}
