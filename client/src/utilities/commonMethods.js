const IsListEmpty = (list) => {
  if (
    list !== undefined &&
    list !== null &&
    list !== "null" &&
    list.length > 0
  ) {
    return false;
  }
  return true;
};

const IsObjectEmpty = (obj) => {
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) return false;
  }
  return true;
};

const IsStringEmpty = (str) => {
  if (str !== undefined && str !== null && str !== "null" && str !== "") {
    return false;
  }
  return true;
};

export { IsListEmpty, IsObjectEmpty, IsStringEmpty };
