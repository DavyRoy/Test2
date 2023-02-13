export function getCheckPoints(state) {
  return state.checkPoints;
}

export function getProjects(state) {
  return state.projects;
}

export const getCheckPointById = (state) => (checkpointId) => {
  return state.checkPoints.find((checkPoint) => checkPoint.id === checkpointId);
};

export function getStages(state) {
  return state.checkPoints.filter(checkPoint => checkPoint.is_stage)
}
