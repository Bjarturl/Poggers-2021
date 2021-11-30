export const formatArrByKey = (arr, key) => {
  return arr.map((subObj) => subObj[key]);
};

export const capitalizeFirstLetter = (str) => {
  return (
    str[0].toUpperCase() + str.split("_").join(" ").substring(1, str.length)
  );
};

export const getChartData = (baseObj, key, x, y) => {
  return {
    labels: formatArrByKey(baseObj, x),
    lines: {
      data: formatArrByKey(baseObj, y),
      label: capitalizeFirstLetter(key),
    },
  };
};
