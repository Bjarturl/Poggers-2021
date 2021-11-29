export const formatArrByKey = (arr, key) => {
  return arr.map((subObj) => subObj[key]);
};

export const capitalizeFirstLetter = (str) => {
  return (
    str[0].toUpperCase() + str.split("_").join(" ").substring(1, str.length)
  );
};
