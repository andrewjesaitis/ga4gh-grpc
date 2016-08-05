from __future__ import print_function

from grpc.beta import implementations
import google.protobuf.json_format as json_format

import ga4gh.variant_service_pb2 as variant_service_pb2

_TIMEOUT_SECONDS = 10

def chr1_variants(channel):
  reference = 'NCBI37'
  start = 0
  end = 249250620

  stub = variant_service_pb2.beta_create_VariantService_stub(channel)
  req = variant_service_pb2.SearchVariantsRequest(
    reference_name=reference,
    start=start,
    end=end
  )

  print("Searching for Variants on Chromosome 1...")
  for variant in stub.SearchVariants(req, None):
    print(variant)
    # print(json_format.MessageToJson(variant))


def run():
  channel = implementations.insecure_channel('localhost', 50051)
  chr1_variants(channel)


if __name__ == '__main__':
  run()
