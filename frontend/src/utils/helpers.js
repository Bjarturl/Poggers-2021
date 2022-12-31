export const formatArrByKey = (arr, key) => {
  return arr.map((subObj) => subObj[key]);
};

export const capitalizeFirstLetter = (str) => {
  return (
    str[0].toUpperCase() + str.split("_").join(" ").substring(1, str.length)
  );
};

export const getTrueLabel = (str) => {
  const key = str.toLowerCase()
  const labels = {
    'fjoldi skilaboda eftir tima dags': 'Fjöldi skilaboða eftir tíma dags',
    'fekk flest reactions': 'Fékk flest reactions',
    'fjoldi skilaboda eftir degi': 'Fjöldi skilaboða eftir degi',
    'reactadi oftast': 'Reactaði oftast',
    'medallengd skilaboda i ordum': 'Meðallengd skilaboða í orðum',
    'flestar myndir sendar': 'Flestar myndir sendar',
    'fjoldi skilaboda eftir manudum': 'Fjöldi skilaboða eftir mánuðum',
    'lengstu skilabodin i ordum': 'Lengstu skilaboðin í orðum',
    'flest skilabod send': 'Flest skilaboð send',
    'heildarfjoldi mynda': 'Heildarfjöldi mynda',
    'reactions per einstaklingur': 'Reactions per einstaklingur',
    'lengstu skilaboðin i ordum': 'Lengstu skilaboðin í orðum',
  }
  return labels[key]
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
