
"use strict";

let GetOriginSphericalCoord = require('./GetOriginSphericalCoord.js')
let TransformFromSphericalCoord = require('./TransformFromSphericalCoord.js')
let SetCurrentDirection = require('./SetCurrentDirection.js')
let SetOriginSphericalCoord = require('./SetOriginSphericalCoord.js')
let SetCurrentModel = require('./SetCurrentModel.js')
let GetCurrentModel = require('./GetCurrentModel.js')
let TransformToSphericalCoord = require('./TransformToSphericalCoord.js')
let SetCurrentVelocity = require('./SetCurrentVelocity.js')

module.exports = {
  GetOriginSphericalCoord: GetOriginSphericalCoord,
  TransformFromSphericalCoord: TransformFromSphericalCoord,
  SetCurrentDirection: SetCurrentDirection,
  SetOriginSphericalCoord: SetOriginSphericalCoord,
  SetCurrentModel: SetCurrentModel,
  GetCurrentModel: GetCurrentModel,
  TransformToSphericalCoord: TransformToSphericalCoord,
  SetCurrentVelocity: SetCurrentVelocity,
};
