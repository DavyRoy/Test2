export const generateColor = (opacity) => {
  const x = Math.floor(Math.random() * (220 - 80)) + 80;
  const y = Math.floor(Math.random() * (220 - 80)) + 80;
  const z = Math.floor(Math.random() * (220 - 80)) + 80;
  return `rgba(${x}, ${z}, ${y}, ${opacity})`;
};
