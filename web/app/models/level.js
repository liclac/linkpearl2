import DS from 'ember-data';

export default DS.Model.extend({
  level: DS.attr('number'),
  exp_at: DS.attr('number'),
  exp_of: DS.attr('number'),
  character: DS.belongsTo('character'),
  job: DS.belongsTo('job', { async: true }),
});
